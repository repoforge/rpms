# $Id$
# Authority: dag

Summary: Build new RPM packages from an old installed package
Name: rpmrebuild
Version: 1.4.6
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://rpmrebuild.sourceforge.net/

# Source: http://dl.sf.net/rpmrebuild/rpmrebuild-%{version}-1.src.rpm
Source: rpmrebuild.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: rpm

%description
you have an installed package on a computer, want to install on other
one, and do not find the rpm file anymore.
Or you want to distribute your customization in an rpm format
this tool is for you.

%prep
%setup -c %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#make ROOT="$RPM_BUILD_ROOT" install
%makeinstall

#%postun
##echo "%postun $1"
#
#[ $1 -ne 0 ] && exit 0 || :
#########################################
## This code should remove all lines from
## the line contains 'RPMREBUILD START'
## till (include) line 'RPMREBUILD END'
## in the file /etc/popt
#########################################
#rm -f /etc/popt.tmp || exit
#
#if [ -f /etc/popt ]; then
#   (
#      need_copy=1
#      while :; do
#         if ! read line; then
#            [ "x$line" = "x" ] && break
#         fi
#         case "x$line" in
#            x*RPMREBUILD*START*) need_copy="" ; continue;;
#            x*RPMREBUILD*END*)   need_copy="1"; continue;;
#         esac
#         [ "$need_copy" ] && { echo "$line" || exit; } || :
#      done
#   ) < /etc/popt > /etc/popt.tmp || exit
#   if [ -s /etc/popt.tmp ]; then
#      mv -f /etc/popt.tmp /etc/popt || exit
#   else
#      rm -f /etc/popt.tmp /etc/popt || exit
#   fi
#else
#  :
#fi
#
#%triggerin -- rpm < 4.0.3
##echo "%triggerin -- rpm < 4.0.3 ('$1' '$2')"
#
#########################################
## This code should remove all lines from
## the line contains 'RPMREBUILD START'
## till (include) line 'RPMREBUILD END'
## in the file /etc/popt
#########################################
#rm -f /etc/popt.tmp || exit
#
#if [ -f /etc/popt ]; then
#   (
#      need_copy=1
#      while :; do
#         if ! read line; then
#            [ "x$line" = "x" ] && break
#         fi
#         case "x$line" in
#            x*RPMREBUILD*START*) need_copy="" ; continue;;
#            x*RPMREBUILD*END*)   need_copy="1"; continue;;
#         esac
#         [ "$need_copy" ] && { echo "$line" || exit; } || :
#      done
#   ) < /etc/popt > /etc/popt.tmp || exit
#   if [ -s /etc/popt.tmp ]; then
#      mv -f /etc/popt.tmp /etc/popt || exit
#   else
#      rm -f /etc/popt.tmp /etc/popt || exit
#   fi
#else
#  :
#fi
#cat /usr/lib/rpmrebuild/popt-without-POPTdesc >> /etc/popt || exit
#
#%triggerin -- rpm >= 4.0.3
##echo "%triggerin -- rpm >= 4.0.3 ('$1' '$2')"
#
#########################################
## This code should remove all lines from
## the line contains 'RPMREBUILD START'
## till (include) line 'RPMREBUILD END'
## in the file /etc/popt
#########################################
#rm -f /etc/popt.tmp || exit
#
#if [ -f /etc/popt ]; then
#   (
#      need_copy=1
#      while :; do
#         if ! read line; then
#            [ "x$line" = "x" ] && break
#         fi
#         case "x$line" in
#            x*RPMREBUILD*START*) need_copy="" ; continue;;
#            x*RPMREBUILD*END*)   need_copy="1"; continue;;
#         esac
#         [ "$need_copy" ] && { echo "$line" || exit; } || :
#      done
#   ) < /etc/popt > /etc/popt.tmp || exit
#   if [ -s /etc/popt.tmp ]; then
#      mv -f /etc/popt.tmp /etc/popt || exit
#   else
#      rm -f /etc/popt.tmp /etc/popt || exit
#   fi
#else
#  :
#fi
#cat /usr/lib/rpmrebuild/popt-with-POPTdesc >> /etc/popt || exit

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
/a

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.6-1.2
- Rebuild for Fedora Core 5.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 1.4.6-1
- Updated to release 1.4.6.

* Tue Oct 07 2003 Dag Wieers <dag@wieers.com> - 1.4.5-0
- Initial package. (using DAR)
