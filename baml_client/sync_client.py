###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Any, Dict, List, Optional, TypeVar, Union, TypedDict, Type, Literal, cast
from typing_extensions import NotRequired
import pprint

import baml_py
from pydantic import BaseModel, ValidationError, create_model

from . import partial_types, types
from .types import Checked, Check
from .type_builder import TypeBuilder
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME

OutputType = TypeVar('OutputType')

# Define the TypedDict with optional parameters having default values
class BamlCallOptions(TypedDict, total=False):
    tb: NotRequired[TypeBuilder]
    client_registry: NotRequired[baml_py.baml_py.ClientRegistry]

class BamlSyncClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __stream_client: "BamlStreamClient"

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__stream_client = BamlStreamClient(self.__runtime, self.__ctx_manager)

    @property
    def stream(self):
      return self.__stream_client

    
    def AnalyzeCritic(
        self,
        knowledges: List[types.KnowledgeItem],context: List[str],question: str,
        baml_options: BamlCallOptions = {},
    ) -> str:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "AnalyzeCritic",
        {
          "knowledges": knowledges,"context": context,"question": question,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(str, raw.cast_to(types, types, partial_types, False))
    
    def AnalyzeSteps(
        self,
        diary_context: List[str],
        baml_options: BamlCallOptions = {},
    ) -> types.ErrorAnalysisOutput:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "AnalyzeSteps",
        {
          "diary_context": diary_context,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.ErrorAnalysisOutput, raw.cast_to(types, types, partial_types, False))
    
    def DedupQueries(
        self,
        new_queries: List[str],existing_queries: List[str],
        baml_options: BamlCallOptions = {},
    ) -> types.DedupOutput:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "DedupQueries",
        {
          "new_queries": new_queries,"existing_queries": existing_queries,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.DedupOutput, raw.cast_to(types, types, partial_types, False))
    
    def EvaluateAttribution(
        self,
        question: str,answer: str,source_content: str,
        baml_options: BamlCallOptions = {},
    ) -> types.AttributionAnalysis:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "EvaluateAttribution",
        {
          "question": question,"answer": answer,"source_content": source_content,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.AttributionAnalysis, raw.cast_to(types, types, partial_types, False))
    
    def EvaluateCompleteness(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> types.CompletenessAnalysis:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "EvaluateCompleteness",
        {
          "question": question,"answer": answer,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.CompletenessAnalysis, raw.cast_to(types, types, partial_types, False))
    
    def EvaluateDefinitive(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> types.DefinitiveAnalysis:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "EvaluateDefinitive",
        {
          "question": question,"answer": answer,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.DefinitiveAnalysis, raw.cast_to(types, types, partial_types, False))
    
    def EvaluateFreshness(
        self,
        question: str,answer: str,current_time: str,
        baml_options: BamlCallOptions = {},
    ) -> types.FreshnessAnalysis:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "EvaluateFreshness",
        {
          "question": question,"answer": answer,"current_time": current_time,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.FreshnessAnalysis, raw.cast_to(types, types, partial_types, False))
    
    def EvaluatePlurality(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> types.PluralityAnalysis:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "EvaluatePlurality",
        {
          "question": question,"answer": answer,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.PluralityAnalysis, raw.cast_to(types, types, partial_types, False))
    
    def EvaluateQuestion(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> types.QuestionEvaluationOutput:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "EvaluateQuestion",
        {
          "question": question,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.QuestionEvaluationOutput, raw.cast_to(types, types, partial_types, False))
    
    def ExtractRelevantSegments(
        self,
        passage: types.Passage,
        baml_options: BamlCallOptions = {},
    ) -> types.ExtractedSegments:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractRelevantSegments",
        {
          "passage": passage,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.ExtractedSegments, raw.cast_to(types, types, partial_types, False))
    
    def GenerateAction(
        self,
        knowledges: List[types.KnowledgeItem],question: str,current_date: str,allow_reflect: bool,allow_read: bool,allow_answer: bool,allow_search: bool,all_keywords: List[str],url_list: List[Union[types.StandardSearchResult, types.AlternativeSearchResult]],bad_context: List[types.BadContext],context: Optional[List[str]],
        baml_options: BamlCallOptions = {},
    ) -> types.ActionWithThink:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "GenerateAction",
        {
          "knowledges": knowledges,"question": question,"current_date": current_date,"allow_reflect": allow_reflect,"allow_read": allow_read,"allow_answer": allow_answer,"allow_search": allow_search,"all_keywords": all_keywords,"url_list": url_list,"bad_context": bad_context,"context": context,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.ActionWithThink, raw.cast_to(types, types, partial_types, False))
    
    def GenerateReport(
        self,
        original_question: str,knowledge: List[types.KnowledgeItem],visited_urls: List[Union[types.StandardSearchResult, types.AlternativeSearchResult]],diary_context: Optional[List[str]],current_date: str,references: List[types.Reference],
        baml_options: BamlCallOptions = {},
    ) -> str:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "GenerateReport",
        {
          "original_question": original_question,"knowledge": knowledge,"visited_urls": visited_urls,"diary_context": diary_context,"current_date": current_date,"references": references,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(str, raw.cast_to(types, types, partial_types, False))
    
    def RewriteQuery(
        self,
        query: str,think: str,current_date: str,
        baml_options: BamlCallOptions = {},
    ) -> types.QueryRewriterOutput:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "RewriteQuery",
        {
          "query": query,"think": think,"current_date": current_date,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.QueryRewriterOutput, raw.cast_to(types, types, partial_types, False))
    



class BamlStreamClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager

    
    def AnalyzeCritic(
        self,
        knowledges: List[types.KnowledgeItem],context: List[str],question: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[str], str]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "AnalyzeCritic",
        {
          "knowledges": knowledges,
          "context": context,
          "question": question,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[Optional[str], str](
        raw,
        lambda x: cast(Optional[str], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(str, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def AnalyzeSteps(
        self,
        diary_context: List[str],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.ErrorAnalysisOutput, types.ErrorAnalysisOutput]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "AnalyzeSteps",
        {
          "diary_context": diary_context,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.ErrorAnalysisOutput, types.ErrorAnalysisOutput](
        raw,
        lambda x: cast(partial_types.ErrorAnalysisOutput, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.ErrorAnalysisOutput, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def DedupQueries(
        self,
        new_queries: List[str],existing_queries: List[str],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.DedupOutput, types.DedupOutput]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "DedupQueries",
        {
          "new_queries": new_queries,
          "existing_queries": existing_queries,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.DedupOutput, types.DedupOutput](
        raw,
        lambda x: cast(partial_types.DedupOutput, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.DedupOutput, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def EvaluateAttribution(
        self,
        question: str,answer: str,source_content: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.AttributionAnalysis, types.AttributionAnalysis]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "EvaluateAttribution",
        {
          "question": question,
          "answer": answer,
          "source_content": source_content,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.AttributionAnalysis, types.AttributionAnalysis](
        raw,
        lambda x: cast(partial_types.AttributionAnalysis, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.AttributionAnalysis, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def EvaluateCompleteness(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.CompletenessAnalysis, types.CompletenessAnalysis]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "EvaluateCompleteness",
        {
          "question": question,
          "answer": answer,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.CompletenessAnalysis, types.CompletenessAnalysis](
        raw,
        lambda x: cast(partial_types.CompletenessAnalysis, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.CompletenessAnalysis, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def EvaluateDefinitive(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.DefinitiveAnalysis, types.DefinitiveAnalysis]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "EvaluateDefinitive",
        {
          "question": question,
          "answer": answer,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.DefinitiveAnalysis, types.DefinitiveAnalysis](
        raw,
        lambda x: cast(partial_types.DefinitiveAnalysis, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.DefinitiveAnalysis, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def EvaluateFreshness(
        self,
        question: str,answer: str,current_time: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.FreshnessAnalysis, types.FreshnessAnalysis]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "EvaluateFreshness",
        {
          "question": question,
          "answer": answer,
          "current_time": current_time,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.FreshnessAnalysis, types.FreshnessAnalysis](
        raw,
        lambda x: cast(partial_types.FreshnessAnalysis, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.FreshnessAnalysis, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def EvaluatePlurality(
        self,
        question: str,answer: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.PluralityAnalysis, types.PluralityAnalysis]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "EvaluatePlurality",
        {
          "question": question,
          "answer": answer,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.PluralityAnalysis, types.PluralityAnalysis](
        raw,
        lambda x: cast(partial_types.PluralityAnalysis, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.PluralityAnalysis, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def EvaluateQuestion(
        self,
        question: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.QuestionEvaluationOutput, types.QuestionEvaluationOutput]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "EvaluateQuestion",
        {
          "question": question,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.QuestionEvaluationOutput, types.QuestionEvaluationOutput](
        raw,
        lambda x: cast(partial_types.QuestionEvaluationOutput, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.QuestionEvaluationOutput, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def ExtractRelevantSegments(
        self,
        passage: types.Passage,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.ExtractedSegments, types.ExtractedSegments]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractRelevantSegments",
        {
          "passage": passage,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.ExtractedSegments, types.ExtractedSegments](
        raw,
        lambda x: cast(partial_types.ExtractedSegments, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.ExtractedSegments, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def GenerateAction(
        self,
        knowledges: List[types.KnowledgeItem],question: str,current_date: str,allow_reflect: bool,allow_read: bool,allow_answer: bool,allow_search: bool,all_keywords: List[str],url_list: List[Union[types.StandardSearchResult, types.AlternativeSearchResult]],bad_context: List[types.BadContext],context: Optional[List[str]],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.ActionWithThink, types.ActionWithThink]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "GenerateAction",
        {
          "knowledges": knowledges,
          "question": question,
          "current_date": current_date,
          "allow_reflect": allow_reflect,
          "allow_read": allow_read,
          "allow_answer": allow_answer,
          "allow_search": allow_search,
          "all_keywords": all_keywords,
          "url_list": url_list,
          "bad_context": bad_context,
          "context": context,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.ActionWithThink, types.ActionWithThink](
        raw,
        lambda x: cast(partial_types.ActionWithThink, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.ActionWithThink, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def GenerateReport(
        self,
        original_question: str,knowledge: List[types.KnowledgeItem],visited_urls: List[Union[types.StandardSearchResult, types.AlternativeSearchResult]],diary_context: Optional[List[str]],current_date: str,references: List[types.Reference],
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[str], str]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "GenerateReport",
        {
          "original_question": original_question,
          "knowledge": knowledge,
          "visited_urls": visited_urls,
          "diary_context": diary_context,
          "current_date": current_date,
          "references": references,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[Optional[str], str](
        raw,
        lambda x: cast(Optional[str], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(str, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def RewriteQuery(
        self,
        query: str,think: str,current_date: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.QueryRewriterOutput, types.QueryRewriterOutput]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "RewriteQuery",
        {
          "query": query,
          "think": think,
          "current_date": current_date,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.QueryRewriterOutput, types.QueryRewriterOutput](
        raw,
        lambda x: cast(partial_types.QueryRewriterOutput, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.QueryRewriterOutput, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    

b = BamlSyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)

__all__ = ["b"]