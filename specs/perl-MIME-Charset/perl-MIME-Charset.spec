# $Id$
# Authority: dries
# Upstream: IKEDA Soji <hatuka$nezumi,nu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Charset
%define real_version 1.006002

Summary: Charset Informations for MIME
Name: perl-MIME-Charset
Version: 1.006.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Charset/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Charset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Charset Informations for MIME.

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
%doc ARTISTIC COPYING Changes MANIFEST META.yml README
%doc %{_mandir}/man3/MIME::Charset.3pm*
%doc %{_mandir}/man3/MIME::Charset::JA_JP.3pm*
%dir %{perl_vendorlib}/MIME/
%{perl_vendorlib}/MIME/Charset/
%{perl_vendorlib}/MIME/Charset.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.006.2-1
- Updated to release 1.006.2.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.000-1
- Updated to release 1.000.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 0.044-1
- Updated to release 0.044.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.043-1
- Initial package.
