# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Server

Summary: Net-Server module for perl
Name: perl-Net-Server
Version: 0.93
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Server/

Source: http://www.cpan.org/modules/by-module/Net/Net-Server-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Net-Server module for perl

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README examples/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Server/
%{perl_vendorlib}/Net/Server.pm

%changelog
* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 0.93-1
- Updated to release 0.93.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 0.90-1
- Updated to release 0.90.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.88-1
- Updated to release 0.88.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 0.87-1
- Updated to release 0.87.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.86-0
- Updated to release 0.86.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.85-0
- Updated to release 0.85.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 0.84-0
- Initial package. (using DAR)
