# $Id$
# Authority: dag
# Upstream: Greg Banks <gnb@alphalink.com.au>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Graphical front-end for gcov
Name: ggcov
Version: 0.2.2
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.alphalink.com.au/~gnb/ggcov/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.alphalink.com.au/~gnb/ggcov/ggcov-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gcc

%description
Ggcov is a simple GUI program for browsing test coverage data
from C programs, and is intended to be a graphical replacement
for the gcov program.

Test coverage data is produced by programs which have been built
with "gcc -fprofile-arcs -ftest-coverage", and indicate how
many times each line and branch has been executed, cumulatively
over multiple test runs.

%prep
%setup

### FIXME: -liberty is needed in conjunction with -lbdf to build.
#%{__perl} -pi.orig -e 's|^GGCOV_LIBS = |GGCOV_LIBS = -liberty |' Makefile.in

%{__cat} <<EOF >ggcov.desktop
[Desktop Entry]
Name=Ggcov
Comment=Browse C test coverage data
Icon=ggcov.xpm
Exec=ggcov
Terminal=false
Type=Application
Category=Application;Development;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0644 %{_datadir}/ggcov/logo.xpm %{buildroot}%{_datadir}/pixmaps/ggcov.xpm

%if %{dfi}
        %{__install} -D -m0644 ggcov.desktop %{buildroot}%{_datadir}/gnome/apps/Development/ggcov.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		ggcov.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/ggcov/
%{_datadir}/pixmaps/*.xpm
%if %{dfi}
        %{_datadir}/gnome/apps/Development/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Updated to release 0.2.2.

* Mon Jun 09 2003 Dag Wieers <dag@wieers.com> - 0.1.4-0
- Initial package. (using DAR)
