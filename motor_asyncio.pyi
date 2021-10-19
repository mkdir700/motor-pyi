from motor import core
from motor import docstrings


class AsyncIOMotorClient(core.AgnosticClient):
    
    @property
    def address(self): ...
    
    @property
    def arbiters(self): ...
    
    def close(self): ...
    
    def drop_database(self, name_or_database, session=None):
        """Drop a database.

        Raises :class:`TypeError` if `name_or_database` is not an instance of
        :class:`basestring` (:class:`str` in python 3) or
        :class:`~pymongo.database.Database`.

        :Parameters:
          - `name_or_database`: the name of a database to drop, or a
            :class:`~pymongo.database.Database` instance representing the
            database to drop
          - `session` (optional): a
            :class:`~pymongo.client_session.ClientSession`.

        .. versionchanged:: 3.6
           Added ``session`` parameter.

        .. note:: The :attr:`~pymongo.mongo_client.MongoClient.write_concern` of
           this client is automatically applied to this operation when using
           MongoDB >= 3.4.

        .. versionchanged:: 3.4
           Apply this client's write concern automatically to this operation
           when connected to MongoDB >= 3.4.

        """
        ...
    
    @property
    def event_listeners(self): ...
    
    @property
    def fsync(self):
        __doc__ = docstrings.fsync_doc
    
    def get_database(self, name=None, codec_options=None, read_preference=None,
                     write_concern=None, read_concern=None) -> 'AsyncIOMotorDatabase':
        __doc__ = docstrings.get_database_doc
    
    def get_default_database(self, default=None, codec_options=None,
                             read_preference=None, write_concern=None, read_concern=None) -> 'AsyncIOMotorDatabase':
        __doc__ = docstrings.get_default_database_doc
    
    @property
    def HOST(self): ...
    
    @property
    def is_mongos(self): ...
    
    @property
    def is_primary(self): ...
    
    @property
    async def list_databases(self): ...
    
    @property
    async def list_database_names(self): ...
    
    @property
    def local_threshold_ms(self): ...
    
    @property
    def max_bson_size(self): ...
    
    @property
    def max_idle_time_ms(self): ...
    
    @property
    def max_message_size(self): ...
    
    @property
    def max_pool_size(self): ...
    
    @property
    def max_write_batch_size(self): ...
    
    @property
    def min_pool_size(self): ...
    
    @property
    def nodes(self): ...
    
    @property
    def PORT(self): ...
    
    @property
    def primary(self): ...
    
    @property
    def read_concern(self): ...
    
    @property
    def retry_reads(self): ...
    
    @property
    def retry_writes(self): ...
    
    @property
    def secondaries(self): ...
    
    @property
    async def server_info(self): ...
    
    @property
    def server_selection_timeout(self): ...
    
    async def start_session(
        self,
        causal_consistency=None,
        default_transaction_options=None,
        snapshot=False
    ) -> 'AsyncIOMotorClientSession':
        __doc__ = docstrings.start_session_doc
    
    async def unlock(self, session=None):
        __doc__ = docstrings.unlock_doc


class AsyncIOMotorClientSession(core.AgnosticClientSession):
    """A session for ordering sequential operations.

    Do not create an instance of :class:`MotorClientSession` directly; use
    :meth:`MotorClient.start_session`:

    .. code-block:: python3

      collection = client.db.collection

      async with await client.start_session() as s:
          async with s.start_transaction():
              await collection.delete_one({'x': 1}, session=s)
              await collection.insert_one({'x': 2}, session=s)

    .. versionadded:: 2.0
    """
    
    async def commit_transaction(self): ...
    
    async def abort_transaction(self): ...
    
    async def end_session(self): ...
    
    @property
    def cluster_time(self): ...
    
    @property
    def has_ended(self): ...
    
    @property
    def in_transaction(self): ...
    
    @property
    def options(self): ...
    
    @property
    def operation_time(self): ...
    
    @property
    def session_id(self): ...
    
    def advance_cluster_time(self): ...
    
    def advance_operation_time(self): ...


class AsyncIOMotorDatabase(core.AgnosticDatabase):
    
    async def command(self, command, value=1, check=True,
                      allowable_errors=None, read_preference=None,
                      codec_options=DEFAULT_CODEC_OPTIONS, session=None, **kwargs):
        __doc__ = docstrings.cmd_doc
    
    async def create_collection(self, name, codec_options=None,
                                read_preference=None, write_concern=None,
                                read_concern=None, session=None, **kwargs) -> 'AsyncIOMotorCollection': ...
    
    async def current_op(self, include_all=False, session=None):
        __doc__ = docstrings.current_op_doc
    
    async def dereference(self, dbref, session=None, **kwargs): ...
    
    async def drop_collection(self, name_or_collection, session=None): ...
    
    def get_collection(self, name, codec_options=None, read_preference=None,
                       write_concern=None, read_concern=None) -> 'AsyncIOMotorCollection': ...
    
    async def list_collections(self, session=None, filter=None, **kwargs) -> 'AsyncIOMotorCommandCursor': ...
    
    async def list_collection_names(self, session=None, filter=None, **kwargs) -> List[str]:
        __doc__ = docstrings.list_collection_names_doc
    
    @property
    def name(self): ...
    
    async def profiling_info(self, session=None): ...
    
    async def profiling_level(self, session=None): ...
    
    async def set_profiling_level(self, level, slow_ms=None, session=None,
                                  sample_rate=None, filter=None): ...
    
    async def validate_collection(self, name_or_collection,
                                  scandata=False, full=False, session=None,
                                  background=None): ...
    
    def with_options(self, codec_options=None, read_preference=None,
                     write_concern=None, read_concern=None): ...
    
    @property
    def incoming_manipulators(self): ...
    
    @property
    def incoming_copying_manipulators(self): ...
    
    @property
    def outgoing_manipulators(self): ...
    
    @property
    def outgoing_copying_manipulators(self): ...
    
    def __getitem__(self, name) -> 'AsyncIOMotorCollection': ...
    
    def wrap(self, obj) -> 'AsyncIOMotorCollection': ...


AsyncIOMotorCollection = create_asyncio_class(
    core.AgnosticCollection)


class AsyncIOMotorCollection:
    pass

#
#
# AsyncIOMotorCursor = create_asyncio_class(
#     core.AgnosticCursor)
#
#
# AsyncIOMotorCommandCursor = create_asyncio_class(
#     core.AgnosticCommandCursor)
#
#
# AsyncIOMotorLatentCommandCursor = create_asyncio_class(
#     core.AgnosticLatentCommandCursor)
#
#
# AsyncIOMotorChangeStream = create_asyncio_class(
#     core.AgnosticChangeStream)
#
#
# AsyncIOMotorGridFSBucket = create_asyncio_class(
#     motor_gridfs.AgnosticGridFSBucket)
#
#
# AsyncIOMotorGridIn = create_asyncio_class(
#     motor_gridfs.AgnosticGridIn)
#
#
# AsyncIOMotorGridOut = create_asyncio_class(
#     motor_gridfs.AgnosticGridOut)
#
#
# AsyncIOMotorGridOutCursor = create_asyncio_class(
#     motor_gridfs.AgnosticGridOutCursor)
