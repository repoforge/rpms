# Authority: dag

# Upstream: Daniel Elstner <daniel.elstner@gmx.net>

Summary: A GUI search/replace tool featuring Perl-style regular expressions.
Name: regexxer
Version: 0.6
Release: 0
License: GPL
Group: Applications/Text
URL: http://regexxer.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sourceforge.com/regexxer/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glib2-devel >= 2.0.7, gtk2-devel >= 2.0
BuildRequires: libsigc++-devel >= 1.2, gtkmm2-devel >= 2.0
BuildRequires: pcre >= 3.4

%description
regexxer is a nifty GUI search/replace tool featuring Perl-style
regular expressions.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Dec 07 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Updated to release 0.6.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Updated to release 0.5.

* Thu Jun 05 2003 Dag Wieers <dag@wieers.com> - 0.4-1
- Added docs.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
