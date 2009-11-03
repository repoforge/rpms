# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Advanced, easy to use and extensible WikiEngine
Name: moin
Version: 1.3.5
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://moinmoin.wikiwikiweb.de/

Source: http://dl.sf.net/moin/moin-%{version}.tar.gz
Patch0: moin-1.3.5-xml_newline.patch
Patch1: moin-1.3.5-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2.2
Requires: python >= 2.2.2

Provides: moinmoin = %{version}
Obsoletes: moinmoin <= %{version}-%{release}

%description
MoinMoin is an advanced, easy to use and extensible WikiEngine with a large
community of users. Said in a few words, it is about collaboration on easily
editable web pages.

%prep
%setup
### Remove CR for diff in EL4 and older
%{__perl} -pi.orig -e 's|\r$||' MoinMoin/formatter/xml_docbook.py
%patch0 -p1 -b .xml_newline
%patch1 -p1 -b .config

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README docs/CHANGES* docs/README* docs/*.html docs/licenses/
%{_bindir}/cachecleaner
%{_bindir}/globaledit
%{_bindir}/moin-build-index
%{_bindir}/moin-dump
%{_bindir}/moin-optimize-index
%{_bindir}/pagescleaner
%{_bindir}/print-stats
%{_bindir}/repair-language
%{_datadir}/moin/
%{python_sitelib}/MoinMoin/

%changelog
* Sun Mar 11 2007 Dag Wieers <dag@wieers.com> - 1.3.5-1
- Initial package.
