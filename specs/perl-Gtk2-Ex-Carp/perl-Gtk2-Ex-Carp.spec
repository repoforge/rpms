# $Id$
# Authority: dag
# Upstream: Gavin Brown <moc,ku$nworb,mapson,nivag>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-Carp

Summary: Perl module implements GTK+ friendly die() and warn() functions
Name: perl-Gtk2-Ex-Carp
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Ex-Carp/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-Carp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Gtk2-Ex-Carp is a Perl module implements GTK+ friendly
die() and warn() functions.

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
%doc META.yml README
%doc %{_mandir}/man3/Gtk2::Ex::Carp.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
#%{perl_vendorlib}/Gtk2/Ex/Carp/
%{perl_vendorlib}/Gtk2/Ex/Carp.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
