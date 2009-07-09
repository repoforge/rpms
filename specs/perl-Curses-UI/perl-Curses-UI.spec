# $Id$
# Authority: dries
# Upstream: Shawn Boyette <mdxi$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Curses-UI

Summary: Curses based OO user interface framework
Name: perl-Curses-UI
Version: 0.9607
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Curses-UI/

Source: http://www.cpan.org/modules/by-module/Curses/Curses-UI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Curses)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)

%description
A UI framework based on the curses library. Curses::UI contains
several widgets which can be used to build a user interface.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS Changes INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Curses::UI.3pm*
%doc %{_mandir}/man3/Curses::UI::*.3pm*
%dir %{perl_vendorlib}/Curses/
%{perl_vendorlib}/Curses/UI/
%{perl_vendorlib}/Curses/UI.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.9607-1
- Updated to version 0.9607.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.9605-1
- Updated to release 0.9605.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.9603-1
- Updated to release 0.9603.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 0.9602-1
- Updated to release 0.9602.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.9601-1
- Updated to release 0.9601.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.96-1
- Updated to release 0.96.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Initial package.
