# $Id$
# Authority: shuff
# Upstream: Jamie Wilkinson <jaq$google,com>, Vasilios Hoffman <vasilios$google,com>

Summary: NSS plugin for nsscache
Name: libnss-cache
Version: 0.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://code.google.com/p/nsscache/

Source: http://nsscache.googlecode.com/files/libnss-cache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

Requires: nss

%description
An NSS module which adds supports for file maps with a trailing .cache suffix
(/etc/passwd.cache, /etc/group.cache, and /etc/shadow.cache).

Install the nsscache package for a command-line interface to this module.

%prep
%setup -n %{name}

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install LIBDIR="%{buildroot}%{_libdir}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_libdir}/*.so*

%changelog
* Thu Jul 15 2010 Steve Huff <shuff@vecna.org> - 0.1-1
- Initial package.
