# $Id$
# Authority: dag
# Upstream: Gavin Brown <gbrown$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-PodViewer

Summary: Perl module that implements a Gtk2 widget for displaying Plain old Documentation (POD)
Name: perl-Gtk2-Ex-PodViewer
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-Ex-PodViewer/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-Ex-PodViewer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Locale::gettext)

%description
perl-Gtk2-Ex-PodViewer is a Perl module that implements a Gtk2 widget
for displaying Plain old Documentation (POD).

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
%doc README
%doc %{_mandir}/man1/podviewer.1*
%doc %{_mandir}/man3/Gtk2::Ex::PodViewer.3pm*
%doc %{_mandir}/man3/Gtk2::Ex::PodViewer::Parser.3pm*
%{_bindir}/podviewer
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
%{perl_vendorlib}/Gtk2/Ex/PodViewer/
%{perl_vendorlib}/Gtk2/Ex/PodViewer.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Initial package. (using DAR)
