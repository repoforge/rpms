# Authority: dag

# Upstream: gtk-perl-list@gnome.org

%define rname Gtk2

Summary: Gtk2 module for perl.
Name: perl-Gtk2
Version: 1.00
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gtk2-perl/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.8.0, perl(Glib) >= 1.0.0, perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires: gtk2-devel >= 2.0.0
Requires: perl >= 0:5.8.0

%description
Perl bindings to the 2.x series of the Gtk+ widget set.  This module allows you
to write graphical user interfaces in a perlish and object-oriented way, freeing
you from the casting and memory management in C, yet remaining very close in
spirit to original API.

%prep
%setup -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog Changes LICENSE MANIFEST README TODO examples/ gtk-demo/
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sat Oct 11 2003 Dag Wieers <dag@wieers.com> - 1.00-0
- Updated to release 1.00.

* Sun Sep 10 2003 Dag Wieers <dag@wieers.com> - 0.97-0
- Updated to release 0.97.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Updated to release 0.96.

* Fri Aug 22 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Updated to release 0.95.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.94-0
- Updated to release 0.94.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 0.93-0
- Updated to release 0.93.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Sun Jul 27 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.90-0
- Initial package. (using DAR)
