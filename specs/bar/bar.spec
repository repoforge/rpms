# $Id$
# Authority: yury
# Upstream: Michael Peek <peek-sourceforge-bar$tiem,utk,edu>

Summary: Simple command line tool to display information about a data transfer stream
Name: bar
Version: 1.11.1
Release: 1%{?dist}
License: GPLv2
Group: Development/Tools
URL: http://clpbar.sourceforge.net/
Source: http://downloads.sourceforge.net/project/clpbar/clpbar/%{name}-%{version}/%{name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: make

%description
This is a simple command line tool to display information
about a data transfer stream.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING TODO
%{_bindir}/bar
%{_mandir}/man1/bar.1.gz

%changelog
* Sun Aug 14 2011 Yury V. Zaytsev <yury@shurup.com> - 1.11.1-1
- Initial RPM release (Bjarne Saltbaek).
- Minor adjustments for RepoForge.
