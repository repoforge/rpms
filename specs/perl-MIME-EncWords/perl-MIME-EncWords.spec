# $Id$
# Authority: dries
# Upstream: &#20108;&#21313;&#26085;&#9734;&#40736; - IKEDA Soji <hatuka$nezumi,nu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-EncWords

Summary: Deal with RFC-1522 encoded words
Name: perl-MIME-EncWords
Version: 1.002
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-EncWords/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-EncWords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Deal with RFC-1522 encoded words.

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
%doc ARTISTIC Changes MANIFEST META.yml README
%doc %{_mandir}/man3/MIME::EncWords.3pm*
%dir %{perl_vendorlib}/MIME/
#%{perl_vendorlib}/MIME/EncWords/
%{perl_vendorlib}/MIME/EncWords.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 1.002-1
- Updated to release 1.002.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.040-1
- Initial package.
