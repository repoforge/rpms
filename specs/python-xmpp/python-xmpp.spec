# $Id$
# Authority: shuff
# Upstream: Alexey Nezhanov <snake$penza-gsm,ru>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name xmpppy

Name: python-xmpp
Version: 0.4.1
Release: 1%{?dist}
Summary: XMPP-IM-compliant library for jabber instant messenging
Group: Development/Languages
License: GPL
URL: http://xmpppy.sourceforge.net/

Source: http://downloads.sourceforge.net/project/xmpppy/xmpppy/%{version}/xmpppy-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: python-setuptools 

Requires: python-dns

Provides: xmpppy = %{version}-%{release}

%description
This library provides functionality for writing xmpp-compliant clients, servers
and/or components/transports.

It was initially designed as a "rework" of the jabberpy library but has become
a separate product.

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
%doc ChangeLog README
%{python_sitelib}/*
# if arch-specific
# %{python_sitearch}/*

%changelog
* Wed Aug 03 2011 Steve Huff <shuff@vecna.org> - 0.4.1-1
- Initial package.
