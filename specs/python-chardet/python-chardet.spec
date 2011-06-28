# $Id$
# Authority: shuff
# Upstream: Mark Pilgrim <mark$diveintomark,org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name chardet

Name: python-chardet
Version: 2.0.1
Release: 1%{?dist}
Summary: Python Universal Encoding Detector
Group: Development/Languages
License: GPL
URL: http://chardet.feedparser.org/

Source: http://chardet.feedparser.org/download/python2-chardet-%{version}.tgz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: python-setuptools 

Provides: chardet = %{version}-%{release}

%description
Character encoding auto-detection in Python 2 and 3. As smart as your browser.
Open source.

This library is a port of the auto-detection code in Mozilla. I have attempted
to maintain as much of the original structure as possible (mostly for selfish
reasons, to make it easier to maintain the port as the original code evolves).
I have also retained the original authors? comments, which are quite extensive
and informative.

%prep
%setup -n python2-%{real_name}-%{version}

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
* Tue Jun 28 2011 Steve Huff <shuff@vecna.org> - 2.0.1-1
- Initial package.
