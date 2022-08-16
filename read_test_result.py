import argparse
import json

def main():
  parser = argparse.ArgumentParser(description='Build for iOS and tvOS.')
  parser.add_argument('-r', '--test_result', default=None)
  args = parser.parse_args()
  print("--test_result: %s" % args.test_result)
  test_result = json.loads(args.test_result)
  for result in test_result:
    print("return_code: %s; ftl_link: %s" % (result.get("return_code"), result.get("ftl_link")))

if __name__ == '__main__':
  main()
