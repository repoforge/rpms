# $Id$
# Authority: dries
# Upstream: Daniel Milstein <dmilstein$users,sf,net>

Summary: Tool that helps in the creation of packages
Name: packer
Version: 0.1.4
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://packer.sourceforge.net

Source: http://dl.sf.net/packer/packer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Packer is a tool that helps in the creation of packages. It works by asking 
the user for information about a program, and then by generating files 
needed to create Debian, RPM, Slackware, and Autopackage (distribution 
independent installers) packages based off of that information. Unlike 
similar tools, it generates files that are of comparable quality to those 
that are hand-crafted.

%prep
%setup

%build
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__mv} %{buildroot}%{_datadir}/doc/packer packerrpmdocs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING packerrpmdocs/*
%doc %{_mandir}/man1/*
%{_bindir}/desktop2menu
%{_bindir}/differ
%{_bindir}/packer
%{_datadir}/packer/

%changelog
* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.4-1
- Initial package.
