# $Id$
# Authority: shuff
# Upstream: Reuben Thomas <rrt$sc3d,org>

%define luaversion %(echo `pkg-config --variable=V lua`)
%define lualibdir %{_libdir}/lua/%{luaversion}
%define luadatadir %{_datadir}/lua/%{luaversion}

Summary: Lua bindings for POSIX APIs
Name: luaposix
Version: 5.1.11
Release: 1%{?dist}
License: Public Domain
Group: Applications/Development
URL: https://github.com/rrthomas/luaposix/

Source: http://luaforge.net/frs/download.php/4813/luaposix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: lua-devel >= 5.1
BuildRequires: make
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: lua >= 5.1

%description
A POSIX library for Lua.

%prep
%setup -n luaposix

# fix the makefile
%{__perl} -pi -e "s|^PREFIX=.*$|PREFIX=%{_prefix}|;" Makefile
%{__perl} -pi -e "s|^LUALIB=.*$|LUALIB=%{lualibdir}|;" Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog.old README
%{lualibdir}/*

%changelog
* Fri Jul 15 2011 Steve Huff <shuff@vecna.org> - 5.1.11-1
- Initial package.
