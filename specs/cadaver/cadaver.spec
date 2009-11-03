# $Id$
# Authority: dag
# Upstream: Joe Orton <joe@orton.demon.co.uk>

# ExcludeDist: fc1 fc2 fc3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh9:%define _without_pie 1}
%{?rh7:%define _without_pie 1}
%{?el2:%define _without_pie 1}

Summary: Command-line WebDAV client
Name: cadaver
Version: 0.22.5
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.webdav.org/cadaver/

Source: http://www.webdav.org/cadaver/cadaver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: neon-devel >= 0.24.0-1

%description
cadaver is a command-line WebDAV client, with support for file upload,
download, on-screen display, in-place editing, namespace operations
(move/copy), collection creation and deletion, property manipulation,
and resource locking.

%prep
%setup

%build
%configure \
	--with-neon="%{_prefix}" \
%{!?_without_pie:LDFLAGS=-pie} \
%{!?_without_pie:CFLAGS="%{optflags} -fpie"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING FAQ NEWS README THANKS TODO
%doc %{_mandir}/man1/cadaver.1*
%{_bindir}/cadaver

%changelog
* Tue Jan 23 2007 Dag Wieers <dag@wieers.com> - 0.22.5-1
- Updated to release 0.22.5.

* Sat Dec 04 2004 Dag Wieers <dag@wieers.com> - 0.22.2-1
- Updated to release 0.22.2.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 Joe Orton <jorton@redhat.com> 0.22.1-2
- build as PIE

* Tue Apr 20 2004 Joe Orton <jorton@redhat.com> 0.22.1-1
- update to 0.22.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Oct  3 2003 Joe Orton <jorton@redhat.com> 0.22.0-1
- update to 0.22.0; use system neon

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.21.0-2
- rebuild

* Mon Jul 21 2003 Joe Orton <jorton@redhat.com> 0.21.0-1
- update to 0.21.0

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.20.5-5
- rebuild

* Fri Nov 22 2002 Joe Orton <jorton@redhat.com> 0.20.5-4
- force use of bundled neon (#78260)

* Mon Nov  4 2002 Joe Orton <jorton@redhat.com> 0.20.5-3
- rebuild in new environment

* Fri Aug 30 2002 Joe Orton <jorton@redhat.com> 0.20.5-2
- update to 0.20.5; many bug fixes, minor security-related
 fixes, much improved SSL support, a few new features.

* Thu Aug 22 2002 Joe Orton <jorton@redhat.com> 0.20.4-1
- add --with-force-ssl

* Wed May  1 2002 Joe Orton <joe@manyfish.co.uk>
- add man page

* Sat Jan 19 2002 Joe Orton <joe@manyfish.co.uk>
- updated description

* Mon Nov 19 2001 Joe Orton <joe@manyfish.co.uk>
- Merge changes from Nalin Dahyabhai <nalin@redhat.com>.

* Fri Feb 11 2000 Joe Orton <joe@orton.demon.co.uk>
- Text descriptions modified

* Thu Feb 10 2000 Lee Mallabone <lee0@callnetuk.com>
- Initial creation.
