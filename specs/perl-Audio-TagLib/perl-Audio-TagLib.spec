# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-TagLib

Summary: Perl library for reading and editing audio meta data, commonly known as tags. 
Name: perl-Audio-TagLib
Version: 1.42
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-TagLib/

Source: http://www.cpan.org/modules/by-module/Audio/Audio-TagLib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 3:5.8.3, taglib-devel, gcc-c++, perl(ExtUtils::MakeMaker)

%description
Perl library for reading and editing audio meta data, commonly known as tags.

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
%doc Bugs Changes LICENSE* README TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Audio/
%{perl_vendorarch}/Audio/TagLib.pm
%{perl_vendorarch}/Audio/TagLib/
%dir %{perl_vendorarch}/auto/Audio/
%{perl_vendorarch}/auto/Audio/TagLib/

%changelog
* Mon Jun 26 2006 Dag Wieers <dag@wieers.com> - 1.42-1
- Initial package. (using DAR)
