# $Id$

# Authority: dag

# Upstream: <warder@warder.ath.cx>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A GNOME frontend for the v4l (Video For Linux) functions of transcode.
Name: gv4l
Version: 1.0.0
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://warderx.ath.cx:81/projects/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://warderx.ath.cx:81/projects/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: transcode

%description
Gv4l is a gui frontend for the v4l (Video For Linux) functions of transcode.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Gv4l
Comment=%{summary}
Icon=gv4l/gv4l.png
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
EOF

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
        %{__install} -m0644 -%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category AudioVideo                  \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/pixmaps/gv4l/gv4l.png
%if %{dfi}
	%{_datadir}/gnome/apps/Multimedia/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
