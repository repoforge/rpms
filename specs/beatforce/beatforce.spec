# $Id$
# Authority: dag
# Upstream: Patrick Prasse <patrick.prasse@gmx.net>

%define real_name BeatForce

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Computer DJing system
Name: beatforce
Version: 0.1.5
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://developer.berlios.de/projects/beatforce/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.berlios.de/beatforce/BeatForce-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: gnome-libs-devel, libxml-devel, vrb-devel
BuildRequires: libmad-devel, libid3tag-devel, fftw-devel

Obsoletes: BeatForce

%description
Beatforce is a computer dj-ing system with 2 players, a XML-based song
database, a mixer with manual and auto-fade and some more features.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Make it build with vrb 0.4.0. (Fix upstream please)
%{__perl} -pi.orig -e 's|^(\s+vrb)(\s+vrb_buf;)|$1_p$2|;' src/ringbuffer.h

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Beat Force DJ System
Comment=Mix beats and sounds realtime
Exec=beatforce
Type=Application
Terminal=false
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF

%build
#{__aclocal}-1.6 -I macros
%{__aclocal} -I macros
%{__autoheader}
%{__autoconf}
%{__automake} -a
%configure \
	--with-plugin-dir="%{_libdir}/beatforce" \
	--with-theme-dir="%{_datadir}/beatforce"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall 
%{__make} DESTDIR="%{buildroot}" install \
	THEME_DIR="%{buildroot}%{_datadir}/beatforce"

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/beatforce/*.a

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS QuickStart README TODO
%{_bindir}/*
%{_libdir}/beatforce/
%{_datadir}/beatforce/
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.1.5-0
- Initial package. (using DAR)
