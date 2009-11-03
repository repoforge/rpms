# $Id$
# Authority: dag
# Upstream: Dongxu Ma <dongxu,ma$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-TagLib

Summary: Perl library for reading and editing audio meta data, commonly known as tags. 
Name: perl-Audio-TagLib
Version: 1.43
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-TagLib/

Source: http://www.cpan.org/modules/by-module/Audio/Audio-TagLib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: perl >= 3:5.8.3
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: taglib-devel
Requires: perl >= 3:5.8.3

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
%doc Bugs Changes INSTALL LICENSE LICENSE.Artistic LICENSE.GPL MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Audio::TagLib.3pm*
%doc %{_mandir}/man3/Audio::TagLib::*.3pm*
%dir %{perl_vendorarch}/Audio/
%{perl_vendorarch}/Audio/TagLib.pm
%{perl_vendorarch}/Audio/TagLib/
%dir %{perl_vendorarch}/auto/Audio/
%{perl_vendorarch}/auto/Audio/TagLib/

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Mon Jun 26 2006 Dag Wieers <dag@wieers.com> - 1.42-1
- Initial package. (using DAR)
