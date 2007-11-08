# $Id$
# Authority: dries
# Upstream: Fayland <fayland$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Han-Stroke

Summary: Retrieve the stroke count of a Chinese character
Name: perl-Lingua-Han-Stroke
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Han-Stroke/

Source: http://search.cpan.org/CPAN/authors/id/F/FA/FAYLAND/Lingua-Han-Stroke-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Retrieve the stroke count of a Chinese character.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/Han/
%{perl_vendorlib}/Lingua/Han/Stroke.pm
%{perl_vendorlib}/Lingua/Han/Stroke/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Updated to release 0.05.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
