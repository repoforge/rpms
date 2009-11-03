# $Id: perl-Net-Server.spec 3685 2005-11-05 18:17:42Z dries $
# Authority: dag
# Upstream: Paul Seamons <perl$seamons,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Server

Summary: Perl module that implements an extensible, general Perl server engine
Name: perl-Net-Server
Version: 0.90
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Server/

Source: http://www.cpan.org/modules/by-module/Net/Net-Server-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
perl-Net-Server is a Perl module that implements an extensible,
general Perl server engine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Server/
%{perl_vendorlib}/Net/Server.pm

%changelog
* Tue Aug 14 2007 Dag Wieers <dag@wieers.com> - 0.90-2
- Re-added 0.90 release for amavisd-new.

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
