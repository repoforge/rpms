# $Id$
# Authority: dag
# Upstream: Robert Spier <rspier$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-GnuPG

Summary: Process email with GPG
Name: perl-Mail-GnuPG
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-GnuPG/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-GnuPG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Mail-GnuPG is a Perl module to process email with GPG.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Mail::GnuPG.3pm*
%dir %{perl_vendorlib}/Mail/
#%{perl_vendorlib}/Mail/GnuPG/
%{perl_vendorlib}/Mail/GnuPG.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
