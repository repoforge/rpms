# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

Summary: Temporary project to work on GnuPG extensions
Name: newpg
Version: 0.9.5
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.gnupg.org/

Source: ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/newpg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgcrypt-devel >= 1.1.8, libksba-devel >= 0.4.6, pth-devel
Requires: %{_bindir}/pinentry
Provides: gpgsm, gpg-agent

%description
NewPG is a temporary project to work on GnuPG extensions.  It will be
merged into the regular GnuPG sources someday.

%prep
%setup

%build
%configure \
	--enable-gpg
%{__make} %{?_smp_mflags}
%{__make} check

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%post
install-info %{_infodir}/gnupg.info.gz %{_infodir}/dir

%postun
if [ $1 -eq 0 ]; then
	install-info --delete %{_infodir}/gnupg.info.gz %{_infodir}/dir
fi

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog NEWS README THANKS TODO VERSION
%doc %{_infodir}/*.info*
%{_bindir}/*
%{_libdir}/newpg/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Initial package. (using DAR)
