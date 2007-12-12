# $Id$
# Authority: dries
# Upstream: Murat Balaban <murat$enderunix,org>
# Screenshot: http://www.enderunix.org/aget/aget-shot.jpg

Summary: Console download accelerator
Name: aget
Version: 0.4
Release: 5.2
License: GPL
Group: Applications/Internet
URL: http://www.enderunix.org/aget/

Source: http://www.enderunix.org/aget/aget-%{version}.tar.gz
Patch: errno-include.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Aget is a multi-threaded download accelerator. It supports HTTP downloads
and can be run from the console.

%prep
%setup
%patch -p1 -b .errno

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 aget %{buildroot}%{_bindir}/aget

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README THANKS TODO
%{_bindir}/aget

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-5.2
- Rebuild for Fedora Core 5.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net> 0.4-4
- More cleanups.
- uncompress the patch (plays better with CVS/SVN).

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.4-3
- specfile cleanup

* Mon Dec 15 2003 Dries Verachtert <dries@ulyssis.org> 0.4-2
- fixed the Summary (thanks to Koenraad Heijlen)

* Fri Dec 12 2003 Dries Verachtert <dries@ulyssis.org> 0.4-1
- first packaging for Fedora Core 1
