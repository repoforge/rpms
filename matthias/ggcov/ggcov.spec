# Authority: dag

# Upstream: Greg Banks <gnb@alphalink.com.au>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: GTK+ front-end for gcov.
Name: ggcov
Version: 0.1.4
Release: 0
License: GPL
Group: Development/Tools
URL: http://www.alphalink.com.au/~gnb/ggcov/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.alphalink.com.au/~gnb/ggcov/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Ggcov
Comment=%{summary}
Icon=%{_datadir}/ggcov/logo.xpm
Exec=%{name}
Terminal=false
Type=Application
EOF

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Development/
        %{__install} -m0644 gnome-%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Development/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category Development                 \
		--dir %{buildroot}%{_datadir}/applications \
		gnome-%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/ggcov/
%if %{dfi}
        %{_datadir}/gnome/apps/Development/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Mon Jun 09 2003 Dag Wieers <dag@wieers.com> - 0.1.4-0
- Initial package. (using DAR)
