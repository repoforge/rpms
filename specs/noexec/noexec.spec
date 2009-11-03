# $Id$
# Authority: dag
# Upstream: Valery Reznic <valery_reznic$users,sf,net>

Summary: Run a process unable to create childs
Name: noexec
Version: 1.1.0
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://noexec.sourceforge.net/

Source: http://dl.sf.net/noexec/noexec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
You want to run a process which will be unable to create a child
(For example you want run less via sudo and disable escaping to the shell)

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS
%doc %{_mandir}/man?/*
%{_bindir}/noexec
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Initial package. (using DAR)
