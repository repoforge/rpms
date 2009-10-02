# $Id$
# Authority: shuff
# Upstream: Kevin C. Krinke <kckrinke$opendoorsoftware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-Dialogs

Summary: Useful tools for Gnome2/Gtk2 Perl GUI design
Name: perl-%{real_name}
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Ex-Dialogs/

Source: http://search.cpan.org/CPAN/authors/id/K/KC/KCK/Gtk2-Ex-Dialogs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Type) >= 0.22
BuildRequires: perl(Gtk2) >= 0.140
BuildRequires: perl(Gtk2::Ex::Utils) >= 0.08
Requires: perl >= 5.8

%description
This module provides the Gtk2::Ex::Dialogs::Message,
Gtk2::Ex::Dialogs::ErrorMsg and Gtk2::Ex::Dialogs::Question classes to the main
application while setting the initial defaults to those specified upon using
Gtk2::Ex::Dialogs.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
%{perl_vendorlib}/Gtk2/Ex/Dialogs/
%{perl_vendorlib}/Gtk2/Ex/Dialogs.pm

%changelog
* Fri Oct 02 2009 Steve Huff <shuff@vecna.org> - 0.11-1
- Initial package didn't build; various fixes.

* Tue May 01 2007 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
