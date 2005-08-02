# $Id$
# Authority: dag
# Upstream: Sebastiano Vigna <vigna$dsi,unimi,it>

Summary: Nice editor
Name: ne
Version: 1.40
Release: 1
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
%{__make} %{?_smp_mflags} -C src \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/ne %{buildroot}%{_bindir}/ne
%{__install} -Dp -m0644 doc/ne.1 %{buildroot}%{_mandir}/man1/ne.1

%{__install} -d -m0755 %{buildroot}%{_infodir}
%{__install} -p -m0644 doc/ne.info* %{buildroot}%{_infodir}

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README doc/default.* doc/*.html doc/ne.txt terms/
%doc %{_mandir}/man1/ne.1*
%doc %{_infodir}/*.info*
%{_bindir}/ne

%files docs
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.pdf doc/*.ps doc/ne.txt

%changelog
* Sat Jul 23 2005 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 1.38-1
- Updated to release 1.38.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 1.32-1
- Initial package. (using DAR)
