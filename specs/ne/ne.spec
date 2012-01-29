# $Id$
# Authority: dag
# Upstream: Sebastiano Vigna <vigna$dsi,unimi,it>

Summary: Nice editor
Name: ne
Version: 2.3
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://ne.dsi.unimi.it/

Source: http://ne.dsi.unimi.it/ne-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel >= 4.0
BuildRequires: texinfo

%description
ne is a free (GPL'd) text editor based on the POSIX standard that runs (we
hope) on almost any UN*X machine. ne is easy to use for the beginner, but
powerful and fully configurable for the wizard, and most sparing in its
resource usage. If you have the resources and the patience to use emacs or the
right mental twist to use vi then probably ne is not for you. However, being
fast, small, powerful and simple to use, ne is ideal for email, editing through
phone line (or slow GSM/GPRS) connections and so on. Moreover, the internal
text representation is very compact--you can easily load and modify very large
files.

%package docs
Summary: Documentation for package %{name}
Group: Documentation

%description docs
This package includes the documentation for package %{name}.

%prep
%setup

%build
#%{__make} %{?_smp_mflags} -C src CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags} OPTS="-ansi %{optflags}"  NE_ANSI="1" NE_POSIX="1"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ne %{buildroot}%{_bindir}/ne
%{__install} -Dp -m0644 doc/ne.1 %{buildroot}%{_mandir}/man1/ne.1
%{__install} -Dp -m0644 doc/ne.info.gz %{buildroot}%{_infodir}/ne.info.gz

%{__install} -dp -m0755 %{buildroot}%{_libdir}/ne/syntax/
%{__cp} -av syntax/* %{buildroot}%{_libdir}/ne/syntax/

%post
/sbin/install-info %{_infodir}/ne.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/ne.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README doc/default.* doc/ne.txt doc/ne/
%doc %{_mandir}/man1/ne.1*
%doc %{_infodir}/ne.info*
%{_bindir}/ne
%{_libdir}/ne/

%files docs
%defattr(-, root, root, 0755)
%doc doc/ne/ doc/*.pdf doc/ne.txt

%changelog
* Tue Nov 15 2011 Dag Wieers <dag@wieers.com> - 2.3-1
- Updated to release 2.3.

* Mon Mar 14 2011 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Updated to release 2.0.3.

* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 1.43-1
- Updated to release 1.43.

* Fri Jan 26 2006 Dag Wieers <dag@wieers.com> - 1.42-1
- Updated to release 1.42.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 1.41-1
- Updated to release 1.41.

* Sat Jul 23 2005 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 1.32-1
- Initial package. (using DAR)
