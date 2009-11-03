# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Notify

Summary: Perl interface to libnotify
Name: perl-Gtk2-Notify
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Notify/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Notify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
BuildRequires: libnotify-devel
BuildRequires: perl
BuildRequires: perl(Cairo::Install::Files)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib::CodeGen)
BuildRequires: perl(Gtk2)
BuildRequires: pkgconfig
Requires: gtk2
Requires: libnotify

%description
Perl interface to libnotify.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Gtk2::Notify.3pm*
%doc %{_mandir}/man3/Gtk2::Notify::index.3pm*
%dir %{perl_vendorarch}/Gtk2/
%{perl_vendorarch}/Gtk2/Notify.pm
%{perl_vendorarch}/Gtk2/Notify.pod
%{perl_vendorarch}/Gtk2/Notify/
%dir %{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/auto/Gtk2/Notify/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
