import argparse
import json

def main():
  test = { "abc": 12 }
  print("test: %s" % test)
  print("test: %s" % json.dumps(test))
  test = { "abc": 12, "def": [{"a":"a", "b":"b"}, {"a":"a", "b":"b"}] }
  print("test: %s" % test)
  print("test: %s" % json.dumps(test))
  parser = argparse.ArgumentParser(description='Build for iOS and tvOS.')
  parser.add_argument('-r', '--test_result', default=None)
  args = parser.parse_args()
  print("--test_result: %s" % args.test_result)
  test_result = json.loads(args.test_result)
  print("test_result: %s" % test_result)
  print("project_id: %s" % test_result.get("project_id"))
  for app in test_result.get("apps"):
    print("return_code: %s; ftl_link: %s" % (app.get("return_code"), app.get("ftl_link")))

if __name__ == '__main__':
  main()
