# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Sexy

Summary: Perl interface to the sexy widget collection
Name: perl-Gtk2-Sexy
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Sexy/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Sexy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Gtk2::TestHelper)
Requires: perl >= 2:5.8.0

%description
Perl interface to the sexy widget collection.

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Gtk2::Sexy::*.3pm*
%dir %{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/auto/Gtk2/Sexy/
%dir %{perl_vendorarch}/Gtk2/
%{perl_vendorarch}/Gtk2/Sexy/
%{perl_vendorarch}/Gtk2/Sexy.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Updated to release 0.03.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
