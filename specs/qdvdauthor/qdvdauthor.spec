# $Id$
# Authority: dries
# Upstream: <qdvdauthor$users,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}

%define real_version 1.1.0

Summary: Frontend for dvdauthor
Name: qdvdauthor
Version: 1.1.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://qdvdauthor.sourceforge.net/

Source: http://dl.sf.net/qdvdauthor/qdvdauthor-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: netpbm-devel, kdelibs-devel, gcc-c++, gettext, xine-lib-devel
%{?fc4:BuildRequires: compat-gcc-32-c++}
Requires: dvdauthor, mjpegtools

%description
'Q' DVD-Author is a GUI frontent for dvdauthor and related tools. The goal is
to provide an easy-to-use, yet powerful and complete interface to generate DVD
menus, slideshows, and videos to burn on a DVD under Linux.

%prep
%setup
%{__perl} -pi -e 's|make;$|#make|g;' configure
%{__perl} -pi -e 's|static int pthread_self|//static int pthread_self|g;' qdvdauthor/log.h

# FIXME: also add .desktop icons for qrender, qslideshow, qplayer?

%{__cat} <<EOF > qdvdauthor.desktop
[Desktop Entry]
Name=qdvdauthor
Comment=frontend for dvdauthor
Exec=qdvdauthor
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%{?fc4:export MAKEPARAM="CXX=g++32"}
./configure --prefix=%{_prefix} --build-qplayer --build-qslideshow
qmake all.pro
%{__make} %{?_smp_mflags} ${MAKEPARAM} CFLAGS="-O2 -Wall" CXXFLAGS="-DQT_THREAD_SUPPORT -O2 -Wall"

%install
%{__rm} -rf %{buildroot}
export INSTALL_ROOT=%{buildroot}
%makeinstall
%{__install} -D bin/qdvdauthor %{buildroot}%{_bindir}/qdvdauthor
%{__install} -D bin/qplayer %{buildroot}%{_bindir}/qplayer
%{__install} -D bin/qrender %{buildroot}%{_bindir}/qrender
%{__install} -D bin/qslideshow %{buildroot}%{_bindir}/qslideshow


%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	qdvdauthor.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README TODO
%{_bindir}/qdvdauthor
%{_bindir}/qrender
%{_bindir}/qplayer
%{_bindir}/qslideshow
%{_datadir}/applications/*.desktop
%{_datadir}/qdvdauthor/

%changelog
* Mon Apr 21 2008 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Sun Jan 13 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-1.2
- Rebuild for Fedora Core 5.

* Fri Dec 23 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.0-1
- Updated to release 0.1.0.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.10-1
- Initial package.
