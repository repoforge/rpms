# $Id$
# Authority: matthias
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-FormFactory

Summary: Framework for Gtk2 perl applications
Name: perl-Gtk2-Ex-FormFactory
Version: 0.65
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
#URL: http://search.cpan.org/dist/Gtk2-Ex-FormFactory/
URL: http://www.exit1.org/Gtk2-Ex-FormFactory/

#Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-FormFactory-%{version}.tar.gz
Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-FormFactory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Gtk2)

%description
Gtk2::Ex::FormFactory is a framework for Perl Gtk2 developers.

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

### Clean up docs
find examples/ tutorial/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/ tutorial/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
%{perl_vendorlib}/Gtk2/Ex/FormFactory/
%{perl_vendorlib}/Gtk2/Ex/FormFactory.pm

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.65-2
- Disabled auto-requires for examples/ and tutorial/.

* Sun Jul  2 2006 Matthias Saou <http://freshrpms.net/> 0.65-1
- Update to 0.65.

* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.64-1
- Update to 0.64.

* Tue Apr 25 2006 Matthias Saou <http://freshrpms.net/> 0.63-1
- Update to 0.63.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 0.62-1
- Update to 0.62.
- Change Source URL to point to exit1 instead of CPAN.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.59-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 0.59-1
- Initial RPM package.

