# $Id$
# Authority: dag
# Upstream: Ross McFarland <rmcfarla$neces,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-Simple-List

Summary: Perl module with bindings to Gtk2's complex MVC list widget
Name: perl-Gtk2-Ex-Simple-List
Version: 0.50
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Ex-Simple-List/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-Simple-List-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Glib::MakeHelper)
BuildRequires: perl(Gtk2)

%description
Gtk2-Ex-Simple-List is a Perl module with bindings
to Gtk2's complex MVC list widget.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
%dir %{perl_vendorlib}/Gtk2/Ex/Simple/
%{perl_vendorlib}/Gtk2/Ex/Simple/List.pm
%{perl_vendorlib}/Gtk2/Ex/Simple/TiedCommon.pm
%{perl_vendorlib}/Gtk2/Ex/Simple/TiedList.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.50-1
- Initial package. (using DAR)
