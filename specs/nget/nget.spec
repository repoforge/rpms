# $Id$
# Authority: dag
# Upstream: Matthew Mueller <donut$dakotacom,net>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Command line NNTP file grabber
Name: nget
Version: 0.27.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://nget.sourceforge.net/

Source: http://dl.sf.net/nget/nget-%{version}+uulib.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pcre-devel, popt, ncurses-devel, zlib-devel, gcc-c++, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
nget is a command line nntp file grabber. It automatically pieces together
multipart postings for easy retrieval, even substituting parts from multiple
servers. Handles disconnects gracefully, resuming after the last part
succesfully downloaded.

%prep
%setup

%build
%configure \
	--with-pcre \
	--with-popt
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc .ngetrc Changelog COPYING FAQ README TODO
%doc %{_mandir}/man1/nget.1*
%doc %{_mandir}/man1/ngetlite.1*
%{_bindir}/nget
%{_bindir}/ngetlite

%changelog
* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 0.27.1-1
- Updated to release 0.27.1.

* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.26-0
- Updated to release 0.26.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.24.2-0
- Initial package. (using DAR)
