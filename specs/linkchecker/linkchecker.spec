# $Id$
# Authority: dag
# Upstream: Bastian Kleineidam <calvin$users,sf,net>

### FIXME: Install man-pages in /

Summary: Check HTML documents for broken links
Name: linkchecker
Version: 1.12.0
Release: 0
License: GPL
Group: Applications/Publishing
URL: http://linkchecker.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/linkchecker/linkchecker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.3
Requires: python >= 2.3

%description
LinkChecker checks HTML documents for broken links.

%prep
%setup

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
%doc FAQ INSTALL LICENSE README TODO WONTDO
%doc create.sql draft-gilman-news-url-00.txt
%doc lconline/ test/

%changelog
* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 1.12.1-0
- Initial package. (using DAR)
