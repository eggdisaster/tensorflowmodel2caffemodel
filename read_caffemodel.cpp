
#include <caffe/caffe.hpp>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>
#include <google/protobuf/text_format.h>
#include <algorithm>
#include <iosfwd>
#include <memory>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include "caffe/common.hpp"
#include "caffe/proto/caffe.pb.h"
#include "caffe/util/io.hpp"
 
using namespace caffe;
using namespace std;
using google::protobuf::io::FileInputStream;
using google::protobuf::io::FileOutputStream;
using google::protobuf::io::ZeroCopyInputStream;
using google::protobuf::io::CodedInputStream;
using google::protobuf::io::ZeroCopyOutputStream;
using google::protobuf::io::CodedOutputStream;
using google::protobuf::Message;
 
int main()
{
	NetParameter proto;
	ReadProtoFromBinaryFile("/home/dell/PycharmProjects/tensorflowmodel2caffemodel/conv3d_deepnetA_sport1m_iter_1900000", &proto);
	WriteProtoToTextFile(proto, "/home/dell/PycharmProjects/tensorflowmodel2caffemodel/conv3d_deepnetA_sport1m_iter_1900000.txt");
	return 0;
}

