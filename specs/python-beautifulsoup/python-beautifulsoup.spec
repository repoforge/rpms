# $Id$
# Authority: shuff
# Upstream: Leonard Richardson <leonardr$segfault,org>
# ExcludeDist: el2 el3
# Rationale: requires Python 2.4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name BeautifulSoup

Name: python-beautifulsoup
Version: 3.2.0
Release: 1%{?dist}
Summary: Python library for screen-scraping HTML
Group: Development/Languages
License: GPL
URL: http://www.crummy.com/software/BeautifulSoup/

Source: http://www.crummy.com/software/BeautifulSoup/download/3.x/BeautifulSoup-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: python(abi) >= 2.4
BuildRequires: python-setuptools 
Requires: python-chardet

Provides: BeautifulSoup = %{version}-%{release}

%description
Beautiful Soup is a Python HTML/XML parser designed for quick turnaround
projects like screen-scraping. Three features make it powerful:

1. Beautiful Soup won't choke if you give it bad markup. It yields a parse tree
that makes approximately as much sense as your original document. This is
usually good enough to collect the data you need and run away.
2. Beautiful Soup provides a few simple methods and Pythonic idioms for
navigating, searching, and modifying a parse tree: a toolkit for dissecting a
document and extracting what you need. You don't have to create a custom parser
for each application.
3. Beautiful Soup automatically converts incoming documents to Unicode and
outgoing documents to UTF-8. You don't have to think about encodings, unless
the document doesn't specify an encoding and Beautiful Soup can't autodetect
one. Then you just have to specify the original encoding. 

Beautiful Soup parses anything you give it, and does the tree traversal stuff
for you. You can tell it "Find all the links", or "Find all the links of class
externalLink", or "Find all the links whose urls match "foo.com", or "Find the
table heading that's got bold text, then give me that text."

Valuable data that was once locked up in poorly-designed websites is now within
your reach. Projects that would have taken hours take only minutes with
Beautiful Soup. 

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Tue Jun 28 2011 Steve Huff <shuff@vecna.org> - 3.2.0-1
- Initial package.
