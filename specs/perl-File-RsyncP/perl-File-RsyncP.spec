# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-RsyncP

Summary: Implementation of an Rsync client
Name: perl-File-RsyncP
Version: 0.68
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-RsyncP/

Source: http://www.cpan.org/modules/by-module/File/File-RsyncP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
File::RsyncP is a perl implementation of an Rsync client.  It is
compatible with Rsync 2.5.5 (protocol version 26).  It can send
or receive files, either by running rsync on the remote machine,
or connecting to an rsyncd deamon on the remote machine.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/*

%changelog
* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.68-1
- Updated to release 0.68.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.66-1
- Updated to release 0.66.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1.2
- Rebuild for Fedora Core 5.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.52-1
- Initial package. (using DAR)
