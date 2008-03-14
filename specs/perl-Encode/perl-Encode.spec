# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Encode

Summary: Perl module that implements character encodings
Name: perl-Encode
Version: 2.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Encode/

Source: http://www.cpan.org/modules/by-module/Encode/Encode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.7.3
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.7.3

%description
perl-Encode is a Perl module that implements character encodings.

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
%doc AUTHORS Changes MANIFEST META.yml README
%doc %{_mandir}/man1/enc2xs.1*
%doc %{_mandir}/man1/piconv.1*
%doc %{_mandir}/man3/Encode.3pm*
%doc %{_mandir}/man3/Encode::*.3pm*
%doc %{_mandir}/man3/encoding.3pm*
%{_bindir}/enc2xs
%{_bindir}/piconv
%{perl_vendorarch}/Encode/
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
%{perl_vendorarch}/auto/Encode/

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release 2.24.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 2.20-1
- Initial package. (using DAR)
