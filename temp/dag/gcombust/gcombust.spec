# Authority: freshrpms
# Upstream: Jonas Munsin <jmunsin@iki.fi>

Summary: A useful GTK+ front-end for mkisofs and cdrecord.
Name: gcombust
Version: 0.1.55
Release: 0
License: GPL
Group: Applications/Archiving
URL: http://www.abo.fi/~jmunsin/gcombust/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.abo.fi/~jmunsin/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk+-devel >= 1.2.0, glib-devel

%description
Gcombust is a GUI front-end for mkisofs, mkhybrid, cdda2wav, cdrecord
and cdlabelgen, written in C using the GTK+ widget set. Gcombust
includes primitive support for controlling the directory (root)
structure and size of the disk image without copying files/symlinking
or writing ten lines of arguments and it can maximize disk usage by
hinting which directories and files to use.

%prep
%setup

%build
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog FAQ.shtml NEWS README* THANKS TODO
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 0.1.55-0
- Updated to release 0.1.55.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 0.1.54-1
- Updated to release 0.1.54. (using DAR)

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 0.1.53-0
- Initial package.
