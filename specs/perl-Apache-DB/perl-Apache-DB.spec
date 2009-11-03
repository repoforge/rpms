# $Id$
# Authority: dag
# Upstream: Frank Wiles <frank$wiles,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DB

Summary: Perl module to run the interactive Perl debugger under mod_perl
Name: perl-Apache-DB
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DB/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-DB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Apache-DB is a Perl module to run the interactive Perl debugger
under mod_perl.

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
%doc Changes MANIFEST META.yml perldb.conf README
%doc %{_mandir}/man3/Apache::DB.3pm*
%doc %{_mandir}/man3/Apache::DProf.3pm*
%doc %{_mandir}/man3/Apache::SmallProf.3pm*
%doc %{_mandir}/man3/Apache::perl5db.3pm*
%dir %{perl_vendorarch}/Apache/
%{perl_vendorarch}/Apache/DB.pm
%{perl_vendorarch}/Apache/DProf.pm
%{perl_vendorarch}/Apache/SmallProf.pm
%{perl_vendorarch}/Apache/perl5db.pl
%dir %{perl_vendorarch}/auto/Apache/
%{perl_vendorarch}/auto/Apache/DB/

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
