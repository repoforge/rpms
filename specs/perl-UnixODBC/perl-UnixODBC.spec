# $Id$
# Authority: dag
# Upstream: Robert Kiesling <rkies$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UnixODBC

Summary: Perl module for unixODBC
Name: perl-UnixODBC
Version: 0.34
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UnixODBC/

Source: http://www.cpan.org/authors/id/R/RK/RKIES/UnixODBC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-UnixODBC is a Perl module for unixODBC.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic README eg/
%doc %{_mandir}/man3/UnixODBC.3pm*
%{perl_vendorarch}/auto/UnixODBC/
%{perl_vendorarch}/UnixODBC.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.33-1
- Initial package. (using DAR)
