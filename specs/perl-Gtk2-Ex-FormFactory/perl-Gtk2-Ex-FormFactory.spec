# $Id$
# Authority: matthias
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-Ex-FormFactory

Summary: Framework for Gtk2 perl applications
Name: perl-Gtk2-Ex-FormFactory
Version: 0.64
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.exit1.org/Gtk2-Ex-FormFactory/
Source: http://www.exit1.org/packages/Gtk2-Ex-FormFactory/dist/Gtk2-Ex-FormFactory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(Gtk2)
BuildArch: noarch

%description
Gtk2::Ex::FormFactory is a framework for Perl Gtk2 developers.


%prep
%setup -n %{real_name}-%{version}
# Make it so that the .pl scripts in %%doc don't add bogus requirements
%{__chmod} -x examples/*.pl tutorial/*.pl


%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod \
           %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes examples/ LICENSE README tutorial/
%dir %{perl_vendorlib}/Gtk2/
%dir %{perl_vendorlib}/Gtk2/Ex/
%{perl_vendorlib}/Gtk2/Ex/FormFactory/
%{perl_vendorlib}/Gtk2/Ex/FormFactory.pm
%{_mandir}/man3/*


%changelog
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

