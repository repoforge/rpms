# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name X11-GUITest

Summary: Perl module providing GUI testing/interaction facilities
Name: perl-X11-GUITest
Version: 0.21
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-GUITest/

Source: http://www.cpan.org/modules/by-module/X11/X11-GUITest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
X11-GUITest is a perl module providing GUI testing/interaction facilities.

%prep
%setup -n X11-GUITest-%{version} 

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
%doc docs/X11-GUITest.txt docs/X11-GUITest.html docs/ToDo docs/Copying
%doc docs/CodingStyle docs/Changes
%doc eg/FindWindowLike.pl eg/TextEditor_1.pl eg/WebBrowser_1.pl
%doc eg/templates/ScriptTemplate.pl
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/X11/
%{perl_vendorarch}/X11/GUITest.pm
%dir %{perl_vendorarch}/auto/X11/
%{perl_vendorarch}/auto/X11/GUITest/

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
