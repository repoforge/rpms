# $Id$
# Authority: dag
# Upstream: Kevin C. Krinke <kckrinke$opendoorsoftware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-Dialogs

Summary: Gtk2-Ex-Dialogs module for perl
Name: perl-Gtk2-Ex-Dialogs
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Ex-Dialogs/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-Dialogs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Gtk2-Ex-Dialogs module for perl.

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
%doc COPYRIGHT Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Gtk2::Ex::Dialogs.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
#%{perl_vendorlib}/Gtk2/Ex/Dialogs/
%{perl_vendorlib}/Gtk2/Ex/Dialogs.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
