from typing import List, Optional

from gridfs import GridFSBucket
from gridfs.grid_file import GridOut, GridIn, _SEEK_SET
from motor import core, motor_gridfs
from motor import docstrings
from pymongo import results
from pymongo.collection import ReturnDocument
from pymongo.database import DEFAULT_CODEC_OPTIONS


# AsyncIOMotorClient = create_asyncio_class(core.AgnosticClient)

class AsyncIOMotorClient(core.AgnosticClient):
    __doc__ = core.AgnosticClient.__doc__
    
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
    
    def __getitem__(self, name) -> 'AsyncIOMotorDatabase': ...


# AsyncIOMotorClientSession = create_asyncio_class(core.AgnosticClientSession)

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


# AsyncIOMotorDatabase = create_asyncio_class(core.AgnosticDatabase)

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


# AsyncIOMotorCollection = create_asyncio_class(core.AgnosticCollection)


class AsyncIOMotorCollection(core.AgnosticCollection):
    
    async def bulk_write(self, requests, ordered=True,
                         bypass_document_validation=False, session=None):
        __doc__ = docstrings.bulk_write_doc
    
    async def count_documents(self, filter, session=None, **kwargs): ...
    
    async def create_index(self, keys, session=None, **kwargs): ...
    
    async def create_indexes(self, indexes, session=None, **kwargs): ...
    
    async def delete_many(self, filter, collation=None, hint=None, session=None) -> results.DeleteResult:
        __doc__ = docstrings.delete_many_doc
    
    async def delete_one(self, filter, collation=None, hint=None, session=None) -> results.DeleteResult:
        __doc__ = docstrings.delete_one_doc
    
    async def distinct(self, key, filter=None, session=None, **kwargs): ...
    
    async def drop(self, session=None): __doc__ = docstrings
    
    async def drop_index(self, index_or_name, session=None, **kwargs): ...
    
    async def drop_indexes(self, session=None, **kwargs): ...
    
    async def estimated_document_count(self, **kwargs): ...
    
    def find(self, *args, **kwargs) -> AsyncIOMotorCursor: ...
    
    def find_raw_batches(self, *args, **kwargs) -> AsyncIOMotorCursor: ...
    
    async def find_one(self, filter=None, *args, **kwargs) -> Optional[dict]:
        __doc__ = docstrings.find_one_doc
    
    async def find_one_and_delete(self, filter,
                                  projection=None, sort=None, hint=None,
                                  session=None, **kwargs):
        __doc__ = docstrings.find_one_and_delete_doc
    
    async def find_one_and_replace(self, filter, replacement,
                                   projection=None, sort=None, upsert=False,
                                   return_document=ReturnDocument.BEFORE,
                                   hint=None, session=None, **kwargs):
        __doc__ = docstrings.find_one_and_replace_doc
    
    async def find_one_and_update(self, filter, update,
                                  projection=None, sort=None, upsert=False,
                                  return_document=ReturnDocument.BEFORE,
                                  array_filters=None, hint=None, session=None,
                                  **kwargs):
        __doc__ = docstrings.find_one_and_update_doc
    
    @property
    def full_name(self): ...
    
    async def index_information(self, session=None):
        __doc__ = docstrings.index_information_doc
    
    async def inline_map_reduce(self, map, reduce, full_response=False, session=None,
                                **kwargs): ...
    
    async def insert_many(self, documents, ordered=True,
                          bypass_document_validation=False, session=None) -> results.InsertManyResult:
        __doc__ = docstrings.insert_many_doc
    
    async def insert_one(self, document, bypass_document_validation=False,
                         session=None) -> results.InsertOneResult:
        __doc__ = docstrings.insert_one_doc
    
    async def map_reduce(self, map, reduce, out, full_response=False, session=None,
                         **kwargs):
        __doc__ = docstrings.mr_doc
    
    @property
    def name(self): ...
    
    async def options(self, session=None): ...
    
    async def reindex(self, session=None, **kwargs):
        __doc__ = docstrings.reindex_doc
    
    async def rename(self, new_name, session=None, **kwargs): ...
    
    async def replace_one(self, filter, replacement, upsert=False,
                          bypass_document_validation=False, collation=None,
                          hint=None, session=None):
        __doc__ = docstrings.replace_one_doc
    
    async def update_many(self, filter, update, upsert=False, array_filters=None,
                          bypass_document_validation=False, collation=None,
                          hint=None, session=None) -> results.UpdateResult:
        __doc__ = docstrings.update_many_doc
    
    async def update_one(self, filter, update, upsert=False,
                         bypass_document_validation=False,
                         collation=None, array_filters=None, hint=None,
                         session=None) -> results.UpdateResult:
        __doc__ = docstrings.update_one_doc
    
    def with_options(self, codec_options=None, read_preference=None,
                     write_concern=None, read_concern=None): ...
    
    async def _async_aggregate(self, *args, **kwargs): ...
    
    async def _async_aggregate_raw_batches(self, *args, **kwargs): ...
    
    async def _async_list_indexes(self, *args, **kwargs): ...


# AsyncIOMotorCursor = create_asyncio_class(core.AgnosticCursor)


class AsyncIOMotorCursor(core.AgnosticCursor):
    
    @property
    def address(self): ...
    
    def collation(self, collation) -> 'AsyncIOMotorCursor': ...
    
    async def distinct(self, key): ...
    
    async def explain(self): ...
    
    def add_option(self, mask) -> 'AsyncIOMotorCursor': ...
    
    def remove_option(self, mask) -> 'AsyncIOMotorCursor': ...
    
    def limit(self, limit) -> 'AsyncIOMotorCursor': ...
    
    def skip(self, limit) -> 'AsyncIOMotorCursor': ...
    
    def max_scan(self, max_scan) -> 'AsyncIOMotorCursor': ...
    
    def sort(self, key_or_list, direction=None) -> 'AsyncIOMotorCursor':
        __doc__ = docstrings.cursor_sort_doc
    
    def hint(self, index) -> 'AsyncIOMotorCursor': ...
    
    def where(self, code) -> 'AsyncIOMotorCursor':
        __doc__ = docstrings.where_doc
    
    def max_await_time_ms(self, max_await_time_ms) -> 'AsyncIOMotorCursor': ...
    
    def max_time_ms(self, max_time_ms) -> 'AsyncIOMotorCursor': ...
    
    def min(self, spec) -> 'AsyncIOMotorCursor': ...
    
    def max(self, spec) -> 'AsyncIOMotorCursor': ...
    
    def comment(self, comment) -> 'AsyncIOMotorCursor': ...
    
    def allow_disk_use(self, allow_disk_use) -> 'AsyncIOMotorCursor': ...
    
    async def _Cursor__die(self, *args, **kwargs): ...


# AsyncIOMotorCommandCursor = create_asyncio_class(core.AgnosticCommandCursor)

class AsyncIOMotorCommandCursor(core.AgnosticCommandCursor):
    pass


# AsyncIOMotorLatentCommandCursor = create_asyncio_class(core.AgnosticLatentCommandCursor)

class AsyncIOMotorLatentCommandCursor(core.AgnosticLatentCommandCursor):
    pass


# AsyncIOMotorChangeStream = create_asyncio_class(core.AgnosticChangeStream)

class AsyncIOMotorChangeStream(core.AgnosticChangeStream):
    
    @property
    def resume_token(self): ...


# AsyncIOMotorGridFSBucket = create_asyncio_class(motor_gridfs.AgnosticGridFSBucket)

class AsyncIOMotorGridFSBucket(GridFSBucket, motor_gridfs.AgnosticGridFSBucket):
    
    async def delete(self, file_id, session=None): ...
    
    async def download_to_stream(self, file_id, destination, session=None): ...
    
    async def download_to_stream_by_name(self, filename, destination, revision=-1,
                                         session=None): ...
    
    async def open_download_stream(self, file_id, session=None) -> AsyncIOMotorGridOut: ...
    
    async def open_download_stream_by_name(self, filename, revision=-1, session=None) -> AsyncIOMotorGridOut: ...
    
    def open_upload_stream_with_id(
        self, file_id, filename, chunk_size_bytes=None, metadata=None,
        session=None) -> AsyncIOMotorGridIn: ...
    
    def open_upload_stream(self, filename, chunk_size_bytes=None,
                           metadata=None, session=None) -> AsyncIOMotorGridIn: ...
    
    async def rename(self, file_id, new_filename, session=None): ...
    
    async def upload_from_stream(self, filename, source, chunk_size_bytes=None,
                                 metadata=None, session=None): ...
    
    async def upload_from_stream_with_id(self, file_id, filename, source,
                                         chunk_size_bytes=None, metadata=None,
                                         session=None): ...


# AsyncIOMotorGridIn = create_asyncio_class(motor_gridfs.AgnosticGridIn)

class AsyncIOMotorGridIn(GridIn, motor_gridfs.AgnosticGridIn):
    
    @property
    def _id(self): ...
    
    async def abort(self): ...
    
    @property
    def chunk_size(self): ...
    
    @property
    def closed(self): ...
    
    async def close(self): ...
    
    @property
    def content_type(self): ...
    
    @property
    def filename(self): ...
    
    @property
    def length(self): ...
    
    @property
    def md5(self): ...
    
    @property
    def name(self): ...
    
    def read(self, size=-1): ...
    
    def readable(self) -> bool: ...
    
    def seekable(self) -> bool: ...
    
    @property
    def upload_date(self): ...
    
    async def write(self, data): ...
    
    def writeable(self) -> bool: ...
    
    async def writelines(self, sequence): ...
    
    async def set(self): ...


# AsyncIOMotorGridOut = create_asyncio_class(motor_gridfs.AgnosticGridOut)
class AsyncIOMotorGridOut(GridOut, motor_gridfs.AgnosticGridOut):
    
    async def _ensure_file(self): ...
    
    @property
    def _id(self): ...
    
    @property
    def aliases(self): ...
    
    @property
    def chunk_size(self): ...
    
    @property
    def close(self): ...
    
    @property
    def content_type(self): ...
    
    @property
    def filename(self): ...
    
    @property
    def length(self): ...
    
    @property
    def md5(self): ...
    
    @property
    def metadata(self): ...
    
    @property
    def name(self): ...
    
    async def read(self, size=-1): ...
    
    def readable(self) -> bool: ...
    
    async def readchunk(self): ...
    
    async def readline(self, size=-1): ...
    
    def seek(self, pos, whence=_SEEK_SET): ...
    
    def seekable(self) -> bool: ...
    
    def tell(self): ...
    
    @property
    def upload_date(self): ...
    
    def write(self, value): ...


# AsyncIOMotorGridOutCursor = create_asyncio_class(motor_gridfs.AgnosticGridOutCursor)

class AsyncIOMotorGridOutCursor(motor_gridfs.AgnosticGridOutCursor):
    pass
